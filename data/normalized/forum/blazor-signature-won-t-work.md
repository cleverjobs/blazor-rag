# Blazor Signature won't work :(

## Question

**Kez** asked on 22 Dec 2022

I'm trying to use the new Blazor Signature feature in a form but the pad isn't letting me draw. Nothing happens when I touch or use the mouse. Why is that? <TelerikForm Model="NewSignoff" Orientation="@FormOrientation" OnValidSubmit="@HandleValidSubmit"> <FormValidation> <DataAnnotationsValidator></DataAnnotationsValidator> </FormValidation> <FormItems> <FormItem Field="@nameof(Signoff.Email)"></FormItem> <FormItem Field="@nameof(Signoff.JobTitle)"></FormItem> <FormItem Field="@nameof(Signoff.Signature)"></FormItem> @* <FormItem Field="@nameof(Signoff.SigSign)"></FormItem>*@<p> <div class="signature-wrapper"> <TelerikSignature Width="600" Class="SigBox" Height="200px" Color="black" ValidateOn="@ValidationType" @bind-Value="@NewSignoff.SigSign"> </TelerikSignature> </div> </FormItems> </TelerikForm> Even when I copy and paste the example to a new razor page, it doesn't work.

### Response

**Stamo Gochev** commented on 27 Dec 2022

Kezi - I assume that our online Signature demos work as expected? Otherwise there is probably a problem with the browser itself. The provided code looks OK and works on this REPL test page, so the problem should be somewhere else. Check for: JavaScript errors incorrect Blazor parameter binding containers that disable pointer events via CSS ( pointer-events:none ) or JavaScript Please provide a runnable test page if you need further assistance.
