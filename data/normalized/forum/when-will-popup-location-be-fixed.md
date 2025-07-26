# When will popup location be fixed?

## Question

**Den** asked on 07 Dec 2023

Telerik + dotnet 8 is really annoying. You cant mark a component as interactive, because that requires a telerikrootcomponent, and you cant put a telerikrootcomponent at the top level because then the specific component cant find the telerikrootcomponent. And the docs [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#wrong-popup-position](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#wrong-popup-position) provide no workaround at all.

## Answer

**Dimo** answered on 07 Dec 2023

Hello Dennis, The TelerikRootComponent was supposed to wrap all page content, so in essence, this is a new problem. I will check with the devs if it's possible to fix this out-of-the-box. In the meantime, a workaround exists, but it's not elegant at all and requires the undesired popup offset to be predictable and consistent. For example, if popups show 100px down and to the right, you can pull them back with: .k-animation-container,.k-window { margin-left: - 100px; margin-top: - 100px;
} Regards, Dimo Progress Telerik

### Response

**Dennis** commented on 08 Dec 2023

Thanks, that work-around works decently enough for the specific case I am currently working on. I won't mark it as an accepted answer though, since it only works in the very specific situation where you can predict the page offset of the child TelerikRootComponent.
