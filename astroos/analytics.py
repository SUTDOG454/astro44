"""PostHog analytics client for AstroOS."""

import atexit
import os
import warnings

from posthog import Posthog

_token = os.environ.get("POSTHOG_PROJECT_TOKEN", "")
_host = os.environ.get("POSTHOG_HOST", "https://us.i.posthog.com")

_debug = os.environ.get("DEBUG", "").lower() in ("1", "true", "yes")

if not _token:
    if _debug:
        warnings.warn(
            "POSTHOG_PROJECT_TOKEN variable required by PostHog is missing or "
            "un-configured, this causes events to be silently missed. "
            "This error stops appearing once POSTHOG_PROJECT_TOKEN is configured",
            stacklevel=2,
        )
    posthog_client = None
else:
    posthog_client = Posthog(
        _token,
        host=_host,
        enable_exception_autocapture=True,
    )
    atexit.register(posthog_client.shutdown)
