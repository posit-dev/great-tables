import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "e2e",
  globalSetup: "./e2e/global-setup.ts",
  forbidOnly: !!process.env.CI,
  reporter: process.env.CI ? "github" : "list",
  // Chromium only for now; WebKit, Firefox and mobile devices come with the host matrix.
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
});
