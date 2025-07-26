
# Breaking Changes in 2.2.0

In the `2.2.0` release, the `Visible` parameter was removed from the `AnimationContainer` component. It was deprecated in favor of methods for showing it some time ago. You should use its `Show()`, `Hide()` and `Toggle()` or `ShowAsync()`, `HideAsync()` and `ToggleAsync()` methods to control its visibility.
