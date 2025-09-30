"""GitHub Projects v2 client stubs for ContextLedger."""

from __future__ import annotations


class ProjectsV2Client:
    """Placeholder GraphQL client for GitHub Projects v2.

    This stub keeps the public interface stable while the original script is
    migrated into the :mod:`contextledger` package. A full implementation should
    authenticate with GitHub and expose a ``query_issues_with_status`` method
    compatible with the legacy usage.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Accept arbitrary arguments for future expansion."""

    def query_issues_with_status(self, *args, **kwargs):
        """Raise a helpful error until the GraphQL implementation is restored."""

        raise NotImplementedError(
            "ProjectsV2Client is a stub. Implement GraphQL queries or disable Projects v2 in config."
        )
