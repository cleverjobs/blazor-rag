# SvgIcon not in the current context

## Question

**BobBob** asked on 02 Sep 2023

Hi there, I knew I must have missed something about this error. I'm trying to using SvgIcon in the grid button but it complained about ""The name 'SvgIcon' does not exist in the current context". Please advise. Here is the demo i'm following: [https://demos.telerik.com/blazor-ui/grid/editing-inline](https://demos.telerik.com/blazor-ui/grid/editing-inline) Thanks, Bob

## Answer

**Bob** answered on 02 Sep 2023

Okay found it. Forgot to include @using Telerik.SvgIcons [https://docs.telerik.com/blazor-ui/common-features/icons](https://docs.telerik.com/blazor-ui/common-features/icons) Bob

### Response

**Flemming** commented on 25 Sep 2024

Thank you Bob!
