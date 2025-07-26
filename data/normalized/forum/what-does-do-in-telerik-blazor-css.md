# What does .\! do in Telerik Blazor CSS?

## Question

**Jos** asked on 19 Jan 2023

Working on some CSS stuff in Telerik for Blazor and see some CSS rules defined like this: .k-this-class { color: green; } .\!k-this-class { color: blue; } What does the .\! do in CSS? Thanks.

### Response

**Ivan Zhekov** commented on 23 Jan 2023

Hello, Joseph. The exclamation mark denotes use of !important flag in the styles. So what you should be seeing should be: .\!k-this-class { color: blue !important } The idea is that some times, you and any other person for that matter, shouldn't worry about specificity when using utility selectors -- you just want something to be always green, always 100% wide etc. In those cases, you can use !className. In this very abstract example -- [https://dojo.telerik.com/@joneff/oJaxIbuh](https://dojo.telerik.com/@joneff/oJaxIbuh) -- I am showing how specificity may affect utility class names, but I am using margin-right, instead of color property. -- Ivan

### Response

**Joseph** commented on 23 Jan 2023

Thank you for the answer. While the answer didn't address my confusion directly, it did make me realize what is happening. The slash (\) is just an escape character and is escaping the exclamation point. So thank you for that.
