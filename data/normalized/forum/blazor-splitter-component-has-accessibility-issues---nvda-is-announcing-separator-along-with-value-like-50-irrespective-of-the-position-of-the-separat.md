# Blazor Splitter Component has accessibility issues - NVDA is announcing separator along with value like "50" irrespective of the position of the separator

## Question

**BB** asked on 31 Oct 2022

Environment Details: URL: Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor Chrome Version 105.0.5195.127 (64-bit) Edge Version 105.0.1343.53 (64-bit) Windows 11 Pro Repro Steps: Go to Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor and hit the "Run" button Turn on NVDA / Narrator Tab till Separator Verify that NVDA / Narrator is announcing separator with a value like "50 separator " or not (regardless of the position of the separator) Actual Result: NVDA is announcing the separator along with a prefix value like "50 " irrespective of the position of the separator Narrator is announcing the current value as 50 irrespective of the position of the separator Expected Result: NVDA / Narrator should announce separator value with respect to position value for the separator (or no separator value at all)

## Answer

**Nadezhda Tacheva** answered on 03 Nov 2022

Hi B, Thank you for sharing detailed information about the behavior you are referring to! The Splitter separator has role="separator" attribute. When such a role is set and the separator is focusable, it is required that aria-valuenow attribute is also set. Currently, the Splitter separator does not have such an attribute and this causes the issue. The linked article does not provide details on the default value of aria-valuenow that is used when this attribute is not explicitly set. However, it looks like this default value is 50. I logged a public bug report on your behalf: [Accessibility] The separator does not have "aria-valuenow" attribute. I added your vote there as we track the community demand along with the issue severity in order to prioritize the bug fixes. As a creator, you are automatically subscribed to receive status updates. Last but not least, I'd like to thank you for reporting this issue. As s small gesture of gratitude, I've rewarded your account with some Telerik points. Regards, Nadezhda Tacheva

### Response

**B** commented on 03 Nov 2022

Thank you!
