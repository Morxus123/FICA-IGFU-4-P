# FICA–IGF-U v3.0 Final Deployment

## Production files

```text
Dockerfile
requirements.txt
main.py
```

## Build

```bash
docker build -t fica-igfu:3.0 .
```

## Run

```bash
docker run --rm -p 8000:8000 fica-igfu:3.0
```

## Smoke checks

```text
/
 /api
 /api/final
 /api/audit/status
 /api/health
 /docs
```

## Measurement checks

`POST /api/measurement/validate`

Example:

```json
{"value": 10.0, "unit": "m", "uncertainty": 0.1}
```

`POST /api/measurement/add`

```json
{
  "a":{"value":10.0,"unit":"m","uncertainty":0.1},
  "b":{"value":5.0,"unit":"m","uncertainty":0.2}
}
```

The result uncertainty is calculated with root-sum-square under the independent-error assumption.
