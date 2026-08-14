# GitHub → CI → Render deployment

## 1. Push this directory to GitHub

```bash
git init
git add .
git commit -m "FICA-IGF-U v3.0 final: CI and Render deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```

## 2. GitHub Actions

`.github/workflows/ci.yml` runs on pushes and pull requests to `main`:

- installs requirements
- compiles `main.py`
- runs `pytest`

## 3. Render

The repository contains `render.yaml`, which defines one Docker web service.

In Render:

1. New → Blueprint
2. Connect the GitHub repository
3. Select `main`
4. Review the Blueprint
5. Deploy Blueprint

The Blueprint uses Docker, Frankfurt, the `/api/health` health check, and `autoDeployTrigger: checksPass`.

Render will therefore wait for the linked CI check to pass before automatically deploying a commit.

## 4. Expected service

After deployment:

```text
https://<service-name>.onrender.com/
https://<service-name>.onrender.com/api
https://<service-name>.onrender.com/api/final
https://<service-name>.onrender.com/api/health
https://<service-name>.onrender.com/docs
```

## 5. Important

Do not commit secrets. Put API keys, database credentials, or other secrets in Render environment variables/GitHub Secrets rather than in source files.
