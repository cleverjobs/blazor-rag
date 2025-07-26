
# Breaking Changes in 9.0.0

## Common

### Trial and commercial users now use the same product package
The trial and commercial product versions merged into a single unified distribution package. The product access now depends on a license key file. This eliminates the need for separate trial downloads. For more information, please refer to the [Telerik License Key](slug:installation-license-key).

### .NET Support

Telerik UI for Blazor 9.0.0 targets .NET 8 and no longer supports .NET 6 and .NET 7. For more information, see [System Requirements](slug:system-requirements).

## Window

The `Centered` parameter is removed. The Window is centered by default if the `Top` and `Left` parameters are equal to an empty string or if they are not set. To center the Window programmatically at any time, [reset the `Top` and `Left` parameter values](slug:components/window/position#top-and-left).
