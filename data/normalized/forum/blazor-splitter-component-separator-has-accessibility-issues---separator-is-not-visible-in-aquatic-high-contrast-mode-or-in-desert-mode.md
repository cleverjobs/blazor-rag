# Blazor Splitter Component separator has accessibility issues - separator is not visible in aquatic high contrast mode or in desert mode

## Question

**BB** asked on 31 Oct 2022

Environment Details: URL: Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor. Edge Version 105.0.1343.53 (64-bit) Windows 11 Pro Control: Blazor Splitter Component | Telerik UI for Blazor Repro Steps: Go to Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor. and hit "Run" Turn on aquatic high contrast mode Verify that in high contrast Aquatic theme, the splitter divider (especially on mouseover) and buttons are completely visible or not. Actual Result: In high contrast Aquatic theme, the splitter and its buttons are not completely visible. Note: Similar issue observed in desert mode - separator is not visible Expected Result: In high contrast Aquatic theme, the splitter divider (especially on mouseover) and buttons should be completely visible

## Answer

**Dimo** answered on 03 Nov 2022

Hello, Yes, you are right. I logged a public bug report on your behalf. The Splitter resizers use a background color, which is removed by High Contrast mode. You can use borders as a workaround: .k-splitter.k-splitbar, /* and/or */.k-splitter.k-resize-handle { border: 1px solid;
} You can also: apply the above style only when high contrast is enabled set a border color, which matches your theme, so that the border is not visible in non-high-contrast mode. Regards, Dimo Progress Telerik

### Response

**B** commented on 03 Nov 2022

Thank you!
