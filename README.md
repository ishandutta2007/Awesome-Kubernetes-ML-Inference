# Awesome-Kubernetes-ML-Inference

## Top Kubernetes ML Inference Ecosystem



**Curated List of SaaS Products & Open-Source GitHub Projects**  

*Focused on Model Serving, GPU Optimization & Production Inference at Scale*  

**Last updated: October 2026**



This repository tracks notable **SaaS platforms** and **open-source projects** for **Kubernetes ML Inference**. These tools deploy, scale, and serve machine learning models — from traditional predictive models to large language models — on Kubernetes with production-grade autoscaling, GPU optimization, and intelligent routing.



**Examples** include Google Vertex AI, AWS SageMaker, Azure Machine Learning, Databricks, Dataiku, DataRobot, H2O.ai, Domino Data Lab, Scale AI, and BentoML (the category leaders).



**Open-source emphasis**: This section is heavily expanded with every major active project for self-hosting, GPU-aware scheduling, and transparent inference infrastructure — ideal for ML engineers, platform teams, and organizations building vendor-neutral Kubernetes-native serving stacks.



Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites.



## Table of Contents

- [SaaS/Hosted Platforms](#saas-hosted-platforms)

- [Open-Source GitHub Projects](#open-source-github-projects)

- [How to Contribute](#how-to-contribute)

- [Disclaimer](#disclaimer)



## Sector Overview & Market Dynamics

The **model-serving platform market** was estimated at **$3.06B in 2025** and is forecast to grow at a **43.3% CAGR through 2030** (Technavio); the broader **AI inference market** it sits inside was valued at **$97.2B in 2024** growing at **17.5% CAGR** (Grand View Research), with the narrower MLOps tooling layer at **$2.2B in 2024** growing at **40.5% CAGR**.

The sector is **moderately fragmented — not winner-take-all**. Model serving alone is called fragmented by analysts, who track 21+ competing vendors, and open-source engines (vLLM, SGLang, KServe, Triton) fragment the serving layer further; concentration appears one level down, where AWS + Microsoft + Google hold ~**63%** of cloud infrastructure (Q3 2025, Synergy), making the hyperscalers the incumbent distribution channel rather than a single serving winner. Switching costs are sticky within deployments, but multi-framework support and cloud portability keep the software layer competitive.

## SaaS/Hosted Platforms

Curated comparison of the leading hosted ML inference / MLOps platforms. All prices are USD unless noted and reflect publicly published rates (list prices, marketplace or procurement listings) as of **October 2026**. Rows are sorted by **company size (descending)** — latest reported revenue where public, otherwise latest disclosed valuation.

| Platform | 🏢 Company Size (revenue / valuation) | Description | 💲 Pricing (specific starting tier) | 🆓 Free Tier / Trial Limits |
|---|---|---|---|---|
| **[Google Vertex AI](https://cloud.google.com/vertex-ai)** | **$402.8B** FY2025 revenue (Alphabet); Google Cloud exited 2025 at a **$70B+** annual run rate | Google's end-to-end ML platform with Model Garden for open models, prediction endpoints, and Vertex AI Agent Builder. Strong integration with GKE for hybrid serving. | Custom prediction endpoints from **$0.077/hour** (`e2-standard-2` basic endpoint) + storage; managed online endpoints billed per node-hour. | Google Cloud **$300 credit for 90 days** (new accounts, applies to Vertex AI); no perpetual free prediction quota. |
| **[Databricks](https://www.databricks.com/)** | **$134B** valuation (Dec 2025, Series L); **$4.8B** revenue run rate | Unified analytics platform with Model Serving for ML models and LLMs, featuring auto-scaling, GPU optimization, and native MLflow integration. | Model Serving on a **T4 GPU = 10.48 DBU/hour**; at the published example rate of **$0.07/DBU** ≈ **$0.73/hour** DBU fee + cloud instance cost. | **Free Edition free forever** (fair-use): serverless-only compute, limited compute size, **no GPU serving**, capped endpoints. Work trial: **14 days, up to $400 credits**. |
| **[AWS SageMaker](https://aws.amazon.com/sagemaker/)** | **$128.7B** FY2025 revenue (AWS) | Fully managed ML platform with real-time inference endpoints, serverless inference, and asynchronous batch transform. Supports Triton, vLLM, and custom containers on EKS. | ML instances from **$0.05/hour** (`ml.t3.medium`); endpoint capacity billed per instance-hour, serverless inference per millisecond. | First **2 months**: **125 hours/month** of real-time inference on `ml.m5.xlarge`/`ml.m4.xlarge` **plus 150,000 seconds/month** serverless inference. |
| **[Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning/)** | **$75B+** FY2025 revenue (Microsoft Azure & other cloud services) | Microsoft's managed ML platform with managed online endpoints, batch inference, and Azure OpenAI Service integration. Native AKS integration for Kubernetes serving. | **$0 ML service surcharge** — you pay Azure compute only; e.g. Microsoft's own training example uses **$1.196/hour** for a `Standard_DS14_v2` VM. | **$200 Azure credit for 30 days** (new accounts, usable on Azure ML compute); no free-forever GPU/compute quota. |
| **[Scale AI](https://scale.com/)** | **~$29B** implied valuation (Jun 2025, Meta's $14.3B for 49%) | Data labeling and model evaluation platform with fine-tuning services and deployment support. | **Rapid self-labeling: $0.05 per labeling unit** after the free allowance (1 annotation = 1 unit); GenAI Platform/GenAI Data Engine priced by custom quote. | **Rapid: 200 free labeling units every month** (free forever); Scale product terms also allow time-boxed trial/evaluation access to GenAI Platform (duration set case-by-case). |
| **[DataRobot](https://www.datarobot.com/)** | **$6.3B** valuation (Jul 2021, Series G) | Automated machine learning platform with deployment, monitoring, and governance features for enterprise AI. | From **£20,000 per license/year** (UK public-sector G-Cloud marketplace listing); direct enterprise pricing is quote-based. | **14-day free trial** (G-Cloud listing); DataRobot docs also describe a **30-day** self-service trial with usage limits. |
| **[H2O.ai](https://h2o.ai/)** | **$1.7B** valuation (Nov 2021, Series E) | Open-source ML platform (with enterprise offerings) featuring Driverless AI for automated model building and deployment. | **H2O AI Cloud on AWS Marketplace: $225,000 per GPU / 12-month contract** (1–64 GPU deployments). | **H2O-3 open source free forever** (Apache 2.0, self-managed, unlimited local use); H2O AI Cloud commercial trial offered (quota not published). |
| **[Domino Data Lab](https://www.domino.ai/)** | **$915.9M** valuation (Aug 2025, Series F) | Enterprise MLOps platform for model development, deployment, and monitoring with reproducibility focus. | AWS Marketplace: **$50,000/year platform fee** + **$62,500/year for 5 practitioner licenses** (published components, before consumption charges). | **No free tier and no published trial** — enterprise-only; evaluation access is arranged via sales. |
| **[Dataiku](https://www.dataiku.com/)** | **$350M+** ARR (Oct 2025) | Enterprise AI platform with visual model development, deployment, and monitoring capabilities across cloud and on-prem environments. | No public list price; published **G-Cloud 14 reseller listing: £101,430 per instance** (Billigence Europe) — enterprise deals are quoted. | **Free Edition free forever** (self-installed, unlimited local use, no published numeric ceilings); Cloud trial **14 days**: 2 users, 1 API service, 4 CPUs, 32 GiB RAM. |
| **[BentoML](https://www.bentoml.com/)** | **$9M** seed (Jun 2023); acquired by **Modular** (Feb 2026, terms undisclosed) | Model serving framework (with hosted BentoCloud) offering adaptive batching, multi-model composition, and scale-to-zero. Python-first with Runner abstraction for custom inference logic. | **BentoCloud pay-as-you-go** (CPU/GPU node-hours, no public rate card since joining Modular in Feb 2026); the open-source framework itself costs **$0**. | **BentoML open source free forever** (Apache 2.0); hosted BentoCloud signup credit **$10 one-time** for new accounts. |



## Open-Source GitHub Projects



- **[KServe](https://github.com/kserve/kserve)**  

  **The standard Kubernetes-native model serving platform** — CNCF project with 5,000+ stars. Provides `InferenceService` CRD abstracting autoscaling, networking, health checking, and server configuration. Supports TensorFlow, PyTorch, XGBoost, scikit-learn, ONNX, and Hugging Face. Features **scale-to-zero**, **canary rollouts**, **GPU autoscaling**, and **multi-node inference** for large LLMs . v0.20 adds confidential model serving with TEE hardware attestation and KV cache offloading for vLLM .



- **[KubeRay / Ray Serve](https://github.com/ray-project/ray)**  

  **Distributed serving on Kubernetes** — Ray Serve builds on Ray to orchestrate multi-model pipelines, heterogeneous GPU workloads, and autoscaling inference services. Excellent for ensemble models combining gradient boosting and neural networks .



- **[NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server)**  

  **High-performance multi-framework inference server** — supports TensorFlow, PyTorch, ONNX, TensorRT, and tree models via FIL backend. Dynamic batching and GPU optimization. Requires external K8s HPA/KEDA for autoscaling (no built-in elasticity) .



- **[Seldon Core v2](https://github.com/SeldonIO/seldon-core)**  

  **Kubernetes model deployment with pipeline DAGs** — v2.x is Apache 2.0 licensed (v1.x was BUSL-1.1, verify version before commercial use). Features drift detection, canary rollouts, and native Experiment/Canary objects for A/B testing .



- **[BentoML](https://github.com/bentoml/BentoML)**  

  **Python-first serving framework** — Runner abstraction for custom inference logic, adaptive batching, and multi-model pipelines. Faster cold starts than KServe for serverless deployments .



- **[vLLM](https://github.com/vllm-project/vllm)**  

  **Production-default LLM inference engine** — PagedAttention for memory-efficient KV cache management, continuous batching, and prefix caching. Red Hat is largest corporate contributor .



- **[SGLang](https://github.com/sgl-project/sglang)**  

  **Fastest inference engine for chat and agents** — RadixAttention for KV cache reuse across related requests. Native disaggregated inference support .



- **[NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo)**  

  **Production-grade disaggregated inference framework** — native prefill/decode separation with RDMA/NVLink KV cache transfer. Supports vLLM, SGLang, and TensorRT-LLM backends at data center scale .



- **[MLOX](https://github.com/MLOX/MLOX)**  

  **Open-source MLOps for small teams and research** — backend-agnostic orchestration supporting Docker, Kubernetes, Native, and Connector backends. Service-centric model: deploy MLflow, Airflow, OpenBao, and MLServer with simple CLI commands. Integrated secrets management and TLS termination. Best for development and testing phases, not large-scale production .



### Additional Strong Open-Source Options



- **[Kubeflow](https://github.com/kubeflow/kubeflow)** — ML toolkit for Kubernetes including Pipelines, Katib (hyperparameter tuning), and KFServing (KServe predecessor) .

- **[NVIDIA NIM](https://www.nvidia.com/en-us/ai/)** — Optimized inference microservices for foundation models; pairs with KServe for deployment orchestration .

- **[Hugging Face TGI](https://github.com/huggingface/text-generation-inference)** — LLM serving with token streaming, continuous batching, and quantization support.

- **[llm-d](https://github.com/llm-d/llm-d)** — Kubernetes-native distributed inference scheduler for disaggregated prefill/decode workloads; complements KServe for cluster-wide KV-cache-aware routing .

- **[LMCache](https://github.com/LMCache/LMCache)** — Distributed KV cache layer for LLM serving; integrates with KServe for reduced TTFT and improved multi-turn QA performance .



**Frameworks for building custom systems**: Combine **KServe** for model lifecycle orchestration, **vLLM** or **SGLang** for inference execution, **llm-d** for cluster-wide routing, and **KEDA** for LLM-specific autoscaling. For multi-framework deployments, layer **Triton** with **KServe** for ensemble models. For lightweight MLOps on Kubernetes, **MLOX** provides integrated secrets and service orchestration .



**Key architectural insight**: The serving stack is layered — **KServe** handles deployment lifecycle and governance, **vLLM/SGLang** handle efficient execution, **llm-d** adds cluster-wide cache-aware routing, and **Triton** serves multi-framework predictive models. For LLM workloads, KServe's `LLMInferenceService` provides OpenAI-compatible endpoints (`/v1/chat/completions`, `/v1/responses`) with KV cache offloading and multi-node tensor parallelism .



## How to Contribute



1. Fork the repo.

2. Add/edit entries in `README.md` (follow existing format).

3. Include: name, link, 1–2 sentence description, and whether it's SaaS or open-source.

4. Submit PR with a short explanation.



Star the repo if you find it useful!



## Disclaimer



- This is a **community-curated** list — not exhaustive and not an endorsement.

- **License awareness is critical**: Seldon Core v1.x is BUSL-1.1 (restricts commercial hosting); v2.x is Apache 2.0. KServe, Triton, BentoML, Ray, vLLM, and SGLang are Apache 2.0 or BSD — safe for commercial use .

- Kubernetes ML inference requires GPU capacity planning, KV cache management, and proper autoscaling configuration for production workloads.

- Self-hosted solutions require Kubernetes operational expertise and regular security updates.



---



**Made for ML engineers, platform architects, AI infrastructure teams, and open-source enthusiasts.**  

Let's make Kubernetes ML inference more open, scalable, and vendor-neutral.

