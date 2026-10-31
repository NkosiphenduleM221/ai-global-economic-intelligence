# AI Global Economic Intelligence Platform

A prototype for exploring macroeconomic indicators and generating plain-language explanations of them, with a path to deploy on Google Cloud.

**Status: early prototype.** The local pipeline runs on sample data, the AI layer is a placeholder, and the GCP infrastructure is defined but not yet deployed. See [What works today](#what-works-today) and [Roadmap](#roadmap) for the exact state.

## What works today

| Component | State |
|---|---|
| Local data pipeline (Python, DuckDB, pandas) | Loads a small set of sample macroeconomic indicators (monthly inflation and GDP growth) into a local DuckDB table, `macro_indicators`. |
| AI service layer (`EconomicIntelligenceLLM`) | Has a deployment mode switch. In `LOCAL_MOCK` mode it returns a templated summary and does **not** call a model or read any documents. The `GCP_VERTEX` mode is a placeholder. |
| Terraform (GCP) | Defines a BigQuery dataset and a Cloud Storage bucket. Not yet applied to a live project. |

## Not built yet

- Ingesting real data (for example, from the World Bank API) instead of sample data
- Loading source documents and generating embeddings
- Retrieval over those documents
- Live Vertex AI calls
- Any model evaluation

## Architecture (target)

```
Source data (World Bank API, reports)
        |
        v
Cloud Storage  -->  BigQuery (indicator tables, embeddings)
                          |
                          v
             Retrieval + LLM explanation service
```

The current code covers the local loading step and the service interface; the rest is the plan.

## Running locally

Requirements: Python 3.10+

```bash
pip install duckdb pandas
```

Run the pipeline module to load the sample data into `economic_intelligence.db`, then run the AI service module to see the mock summary:

```bash
python <path-to-pipeline-module>.py
python <path-to-llm-service-module>.py
```

To select a mode, set `DEPLOYMENT_MODE` (default: `LOCAL_MOCK`).

## Terraform

The `terraform/` folder provisions a BigQuery dataset and a Cloud Storage bucket. Replace the project ID and bucket name with your own before applying, since bucket names are globally unique.

```bash
cd terraform
terraform init
terraform plan
```

## Roadmap

- [ ] Replace sample data with real World Bank indicators
- [ ] Load into BigQuery (a sandbox project is enough)
- [ ] Add document ingestion and embeddings
- [ ] Implement retrieval and a real model call behind `GCP_VERTEX`
- [ ] Add a forecasting model with a train/test split and evaluation metrics
- [ ] Document assumptions, limitations, and failure modes

## Author

Nkosiphendule Mdingi, Johannesburg. GCP Professional Data Engineer and Professional Cloud Architect.
