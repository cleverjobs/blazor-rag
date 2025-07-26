# FluentValidation in Grid PopOut

## Question

**Dar** asked on 20 Oct 2020

Hey, iam evaluating the blazor components for our new project. Our customer has complex validation rules so FluentValidation is for us required. In my PoC i tried to use FluenValidation inside a PopOut but i was not able. Is there a solution to use FluenValidation in the PopOut instead of datanotations? I'm using this package [https://github.com/ryanelian/FluentValidation.Blazor.](https://github.com/ryanelian/FluentValidation.Blazor.) This is my Code <FluentValidator Validator="validator" /> <TelerikGrid Data="personList" Pageable="false" Sortable="true" Resizable="false" EditMode="GridEditMode.Popup" OnUpdate="@UpdateOrCreateHandler" OnDelete="@DeleteHandler" OnCreate="@UpdateOrCreateHandler"> ... </TelerikGrid> private List<Person> personList; PersonValidator validator=new PersonValidator(); With the component call "<FluentValidator Validator="validator" />" i get this error: blazor.webassembly.js:1 crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: DataAnnotationsValidator requires a cascading parameter of type EditContext. For example, you can use DataAnnotationsValidator inside an EditForm. System.InvalidOperationException: DataAnnotationsValidator requires a cascading parameter of type EditContext. For example, you can use DataAnnotationsValidator inside an EditForm. at Microsoft.AspNetCore.Components.Forms.FluentValidator.OnInitialized () <0x3c7cef0 + 0x00018> in <filename unknown>:0 at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync () <0x306e830 + 0x00030> in <filename unknown>:0 Is there a solution to work with fluentvalidation?

## Answer

**Marin Bratanov** answered on 20 Oct 2020

Hello Darius, The grid uses the built-in DataAnnotationsValidator that comes with the Blazor framework. Thus, out-of-the-box, it cannot use a third party validator - that would add a dependency, and can break a lot of peoples' code. The grid must use the standard framework features. The solution to use the FluentValidation package is to make a custom edit form where you control all the code, which means you can include the desired validator. You can find an example of such a custom popup form in this sample project: [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form) so you can use it as base and include the validation you want. Regards, Marin Bratanov
