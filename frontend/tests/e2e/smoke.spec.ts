import { test, expect } from "@playwright/test";

test("homepage loads", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveTitle(/FutureReady/);
  await expect(page.getByText("AI-powered full-stack code generation")).toBeVisible();
});

test("navigation works", async ({ page }) => {
  await page.goto("/");
  await page.getByText("Get Started").click();
  await expect(page).toHaveURL(/.*dashboard/);
});
