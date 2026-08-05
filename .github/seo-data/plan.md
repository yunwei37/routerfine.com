# SEO plan

## Purpose

Build a clear, useful public home for practical routing notes while keeping the
initial implementation deliberately small and measurable.

## Success signals

- Google Analytics 4 records public page activity after deployment.
- Search Console recognizes the domain and sitemap.
- Cloudflare Pages serves the canonical HTTPS URL from the default branch.
- Future pages answer specific routing questions with accurate, durable content.

## Operating constraints

- Raw analytics stay outside Git.
- Every automated change uses a fresh branch and a real non-draft pull request.
- Required and expected CI must pass before the final automated self-review.
- A clean final review is followed by squash merge; human review is not needed.
- Site changes wait for the exact squash commit's production deployment and
  public verification.
- Post-merge evidence is recorded through a metadata-only closeout pull request
  that follows the same CI, self-review, and squash-merge rules.
- Normal operation does not require human approval.
