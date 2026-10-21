# Changelog

## [0.3.0] - 2026-10-21 — Public Launch

### Added
- Multi-sample integration support: **Harmony** (default), scVI, and BBKNN
- `integrate_samples()` function and seamless integration inside `analyze_single_cell()`
- Configuration options for integration method and batch key
- Updated documentation (`docs/SINGLE_CELL.md`, `docs/LAUNCH.md`)
- Launch announcement and ready-to-use social posts

### Changed
- Version bumped to 0.3.0
- README updated to highlight multi-sample capabilities
- Environment includes `harmonypy`

## [0.2.0] - 2026-10-21

### Added
- Single-cell RNA-seq support (Scanpy analysis pipeline)
- STARsolo / Alevin quantification interface
- AI advisor extended for single-cell recommendations
- `docs/SINGLE_CELL.md`

## [0.1.0] - 2026-10-21

### Added
- Initial professional repository structure
- Bulk RNA-seq modules (alignment comparison, quantification, DE)
- AI Parameter Advisor
- Conda environment, Snakemake skeleton, CI, tests, and documentation
