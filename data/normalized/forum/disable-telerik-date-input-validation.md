# Disable Telerik Date Input Validation

## Question

**Har** asked on 26 Sep 2024

Hello Telerik Community, I'm currently working on a Blazor application using the Telerik UI components, and I've run into an issue regarding the default validation behavior of the DateInput component. By default, the DateInput performs validation that sometimes interferes with my application's requirements. Problem Description When using the DateInput component, I noticed that it automatically validates the entered date and displays validation messages if the input does not conform to expected formats or ranges. However, I need to customize this behavior and allow users to enter dates without triggering these default validation checks. Steps Taken I've explored various approaches, including: Custom Validation Attributes: Attempted to apply custom validation attributes to override the default behavior. Disabling Validation: Looked for properties or methods to disable validation directly within the DateInput component. Event Handling: Tried handling the OnBlur and OnChange events to manage validation manually. Questions Is there a built-in way to disable the default validation for the DateInput component? If so, what properties or methods should I utilize to achieve this? Are there best practices for implementing custom validation for the DateInput that you would recommend?
