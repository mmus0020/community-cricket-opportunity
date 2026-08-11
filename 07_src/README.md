# Reproducibility

The repository includes the core transformation and modelling scripts that are most useful for reproducing the public-data prototype.

## Suggested order
1. `01_build_master_lga.py`
2. `01b_patch_merribek.py` where required by geography-version handling
3. `03_build_opportunity_model.py`
4. Use the CSV outputs in `04_data/model_outputs/` for segmentation, case-study and dashboard layers.
5. `06_create_final_report.py` contains the report-generation workflow used for the portfolio report.

The analysis was developed iteratively, so not every exploratory notebook/tool call is represented as a standalone script. The source-of-truth analytical outputs, parameter tables and validation registers are preserved in the repository.
