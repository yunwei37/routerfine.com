# routerfine.com

Minimal static website for `https://routerfine.com`, deployed with Cloudflare
Pages.

## Local validation

```bash
python scripts/validate.py
python .github/seo-skills/scripts/validate_seo_data.py --data-root .github/seo-data
```

The shared SEO operating skills are pinned as a Git submodule at
`.github/seo-skills`. Site-specific public operating records live in
`.github/seo-data`.
