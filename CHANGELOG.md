# Changelog

## 1.0.0 (2025-10-11)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/tejass-cerebras/Thing/compare/v0.0.1...v1.0.0)

### Features

* improve future compat with pydantic v3 ([0a38d8e](https://github.com/tejass-cerebras/Thing/commit/0a38d8ed49fa6f29fe508b2895672d93aefa1f42))
* **types:** replace List[str] with SequenceNotStr in params ([f3b36a2](https://github.com/tejass-cerebras/Thing/commit/f3b36a28c00f3de1752670a30a7480d87960f08a))


### Bug Fixes

* avoid newer type syntax ([9d5fc79](https://github.com/tejass-cerebras/Thing/commit/9d5fc79d3e0762e04723fba9c0260a2bb07b9a93))
* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([d592bd5](https://github.com/tejass-cerebras/Thing/commit/d592bd5efca5995a2622c0039072449b4126d6f0))
* do not set headers with default to omit ([a5cc2b6](https://github.com/tejass-cerebras/Thing/commit/a5cc2b65b8cc34b7412a4d2e06bcb458a739e7f3))
* **types:** add missing types to method arguments ([18f2ecf](https://github.com/tejass-cerebras/Thing/commit/18f2ecf628fad1b586d6fc37429ecf4f8095bc78))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([694f291](https://github.com/tejass-cerebras/Thing/commit/694f291e584363a9c499d27402e8bf7f67f9acf5))
* **internal:** add Sequence related utils ([d7652e7](https://github.com/tejass-cerebras/Thing/commit/d7652e7b4855078be1391a77542d5fdb5b4cfed7))
* **internal:** change ci workflow machines ([c8cd4cf](https://github.com/tejass-cerebras/Thing/commit/c8cd4cf0da71dcdadc3920de38b9564fa69a7778))
* **internal:** detect missing future annotations with ruff ([b564151](https://github.com/tejass-cerebras/Thing/commit/b5641516f3328081abc1e07df88dea3951871a11))
* **internal:** move mypy configurations to `pyproject.toml` file ([de4f911](https://github.com/tejass-cerebras/Thing/commit/de4f911567b7abaa1aecb1ba0d5bffa0ca6bce97))
* **internal:** update pydantic dependency ([23826e8](https://github.com/tejass-cerebras/Thing/commit/23826e86ee0626dc4747ab2e0e74ab2545f90341))
* **internal:** update pyright exclude list ([a629071](https://github.com/tejass-cerebras/Thing/commit/a629071939577542cef93e0c7a0fc875cdcbc5f0))
* **tests:** simplify `get_platform` test ([4c2351c](https://github.com/tejass-cerebras/Thing/commit/4c2351cc7e6ddb19864c7bd8f3043213f31dc3c0))
* **types:** change optional parameter type from NotGiven to Omit ([e9d6a4c](https://github.com/tejass-cerebras/Thing/commit/e9d6a4ce56a0178869ea77b7564a08af6df7b964))
* update github action ([52d6897](https://github.com/tejass-cerebras/Thing/commit/52d68975f4a000d66ef359b6f66f826e109b913e))
* update SDK settings ([03eeb13](https://github.com/tejass-cerebras/Thing/commit/03eeb1389f8fb09b7b66e45f5f3dd311875114f7))
* update SDK settings ([27b2892](https://github.com/tejass-cerebras/Thing/commit/27b28929ce7eda71a3951281db5e4b1d2941d01d))
