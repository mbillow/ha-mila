Vendored copy of [milasdk](https://github.com/simbaja/milasdk) (MIT, see LICENSE).

Base: upstream v2026.1.3 (0458a1c) plus "Support gql 4 alongside gql 3.5"
(mbillow/milasdk@30de1cc, proposed upstream as https://github.com/simbaja/milasdk/pull/10).
The only local difference is `__version__ = "2026.11.0"`.
It's vendored because the PyPI release pins `gql<4`, so Home Assistant 2026.11+ (which
ships gql 4) downgrades gql on boot and the integration fails to import. Drop this copy
and go back to the `milasdk` requirement once upstream releases a gql-4-compatible version (that PR merged and on PyPI).
