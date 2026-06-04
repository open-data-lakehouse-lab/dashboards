# Local Static Dashboards

## Why Static HTML?

Static HTML was chosen for the first dashboard foundation because:
- **Zero Configuration**: No server required.
- **Speed**: Instant generation and rendering.
- **Offline**: Works without internet access.
- **Minimal Dependencies**: Only requires Python and a browser.

## Limitations

- **Non-Interactive**: Static HTML doesn't support real-time filtering or drilling down into data (unless built-in with complex JS, which we currently avoid).
- **Manual Generation**: Requires a CLI command to update.
- **Scalability**: Not suitable for visualizing massive amounts of historical data across multiple runs in a single view.

## How to use

Generated dashboards are saved as `index.html`. You can open them directly:

```bash
open dashboard/index.html  # On MacOS
```
Or simply by double-clicking the file in your file explorer.
