"""Basic tests for the pipeline interface."""

import pandas as pd
from pathlib import Path

from pipeline.align import compare_aligners
from pipeline.advisor import AIParameterAdvisor


def test_advisor():
    adv = AIParameterAdvisor()
    advice = adv.suggest(sample_count=6)
    assert advice.aligner in ("star", "hisat2")
    assert advice.quant_method == "salmon"


def test_compare_aligners_interface(tmp_path):
    samples = pd.DataFrame({
        "sample_id": ["s1"],
        "fastq_r1": [str(tmp_path / "s1_R1.fastq")],
        "fastq_r2": [str(tmp_path / "s1_R2.fastq")],
    })
    # Create dummy files
    for f in samples[["fastq_r1", "fastq_r2"]].values.flatten():
        Path(f).touch()

    summary = compare_aligners(samples, reference="dummy", aligners=["star"])
    assert len(summary) == 1
    assert "mapping_rate_%" in summary.columns
