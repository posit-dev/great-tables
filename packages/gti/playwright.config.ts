import { defineConfig, devices } from "@playwright/test";

const MOBILE = /mobile\.spec\.ts/;
const HOSTS = /hosts\.spec\.ts/;

export default defineConfig({
  testDir: "e2e",
  globalSetup: "./e2e/global-setup.ts",
  forbidOnly: !!process.env.CI,
  reporter: process.env.CI ? "github" : "list",
  // Desktop Chromium, Firefox and WebKit run every spec but the device and host ones. The device one
  // runs on three phones (the narrowest, iPhone SE's, 320px) and a tablet, emulated in Chromium
  // (their size, touch and coarse pointer, not their engine); the host one (the tables shown by
  // Jupyter, Quarto, Shiny, marimo and VS Code) in Chromium
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] }, testIgnore: [MOBILE, HOSTS] },
    { name: "firefox", use: { ...devices["Desktop Firefox"] }, testIgnore: [MOBILE, HOSTS] },
    { name: "webkit", use: { ...devices["Desktop Safari"] }, testIgnore: [MOBILE, HOSTS] },
    { name: "pixel-7", use: { ...devices["Pixel 7"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "iphone-15", use: { ...devices["iPhone 15"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "iphone-se", use: { ...devices["iPhone SE"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "ipad-mini", use: { ...devices["iPad Mini"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "hosts", use: { ...devices["Desktop Chrome"] }, testMatch: HOSTS },
  ],
});
