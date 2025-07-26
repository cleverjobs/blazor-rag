# usage ITelerikStringLocalizer

## Question

**Ste** asked on 08 Aug 2022

Hi, I read all the documentation and downloaded the demo project, but I cannot get the ITelerikStringLocalizer to work in my blazor wasm project. I included the community resource files and made a custom implementation of ITelerikStringLocalizer which I added to the dependency container as singleton in the blazor client project. If I set a breakpoint in this custom implementation I never get a hit. The culture is set at nl-BE, so for some default labels on the Telerik components I would expect the Dutch translation. When checking the teletik datetimepicker I would expect a translation for the marked buttons, I see they are available in the nl-BE resource file. I assume the default english resource file is used, but what could be the reason for this?

## Answer

**Stefan** answered on 08 Aug 2022

Hi, I just found the fix myself. The only difference I still saw with the demo project was the position of where the ITelerikStringLocalizer was added to the dependency container. It seems this needs to be after .AddTelerikBlazor, is there a specific reason for this? I was not aware the order of adding something to the DC could have an impact.

### Response

**Dimo** commented on 10 Aug 2022

Hi Stefan, The declaration order matters, because AddTelerikBlazor registers our default internal localization service, which retrieves the default English strings. According to the Microsoft documentation, the second AddSingleTon call for the same type overrides the first one. public static IServiceCollection AddTelerikBlazor ( this IServiceCollection services ) {
services.AddSingleton<ITelerikStringLocalizer, TelerikStringLocalizer>(); return services;
} This is mentioned in our localization documentation as a comment in a code example, although I agree that we can highlight it a bit more. I have logged a task about it.

### Response

**Stefan** commented on 10 Aug 2022

Hi Dimo, Many thanks for your reply, I completely missed the comment and based on your answer it indeed does make sense.... . kr, Stefan
