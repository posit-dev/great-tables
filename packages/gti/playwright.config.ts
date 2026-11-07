import { defineConfig, devices } from "@playwright/test";

const MOBILE = /mobile\.spec\.ts/;

export default defineConfig({
  testDir: "e2e",
  globalSetup: "./e2e/global-setup.ts",
  forbidOnly: !!process.env.CI,
  reporter: process.env.CI ? "github" : "list",
  // Desktop Chromium runs every spec but the device one, which runs on three phones (the
  // narrowest, iPhone SE's, 320px) and a tablet,
  // emulated in Chromium too (their size, touch and coarse pointer, not their engine); WebKit and
  // Firefox come with the host matrix.
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] }, testIgnore: MOBILE },
    { name: "pixel-7", use: { ...devices["Pixel 7"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "iphone-15", use: { ...devices["iPhone 15"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "iphone-se", use: { ...devices["iPhone SE"], browserName: "chromium" }, testMatch: MOBILE },
    { name: "ipad-mini", use: { ...devices["iPad Mini"], browserName: "chromium" }, testMatch: MOBILE },
  ],
});
