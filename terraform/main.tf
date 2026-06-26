terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "nkosiphendulem221-production"
  region  = "us-central1"
}

resource "google_bigquery_dataset" "economic_warehouse" {
  dataset_id                  = "economic_intelligence_prod"
  location                    = "US"
  description                 = "Production warehouse for global macro trends."
}

resource "google_storage_bucket" "rag_storage" {
  name                        = "nkosiphendulem221-rag-docs"
  location                    = "US"
  uniform_bucket_level_access = true
}
