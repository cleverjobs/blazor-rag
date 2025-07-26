# Accessibility - Reading Order

## Question

**Spe** asked on 10 Apr 2023

We are working accessibility feedback for our site and one of the items we are asked to look at is the reading order. The reader reads our row of labels and then the row of textboxes. (see screenshot) Outside of redoing how we made the page is it possible to indicate the order? I think not, but looking for confirmation before we do anything.

### Response

**Hristian Stefanov** commented on 12 Apr 2023

Hi Spencer, I'm pasting here the answer I gave you in the private ticket so the community can benefit from it.=======I confirm that the current order the screen reader follows stems from the rendering order of the elements/components. Having said this, to achieve the desired result, you need to change the rendering order of the components. Based on the provided screenshot, I have prepared an example for you that shows one possible structure you can use: <div style="display:inline-block;margin-right:10px;"> <label for="phone" style="display: block;"> Phone </label> <TelerikMaskedTextBox @bind-Value="@MaskedValue" Mask="0000-0000-0000-0000" Width="300px" Id="phone" /> </div> <div style="display:inline-block;margin-right:10px;"> <label for="extension" style="display: block;"> Extension </label> <TelerikTextBox @bind-Value="@MaskedValue" Width="150px" Id="extension" /> </div> <div style="display:inline-block;margin-right:10px;"> <label for="email" style="display: block;"> Email </label> <TelerikTextBox @bind-Value="@MaskedValue" Width="150px" Id="email" /> </div> @code {
private string MaskedValue { get; set; }
} Please run and test it to see the result. Let me know if it suits your needs. I'm at your disposal if we can assist further.=======Kind Regards, Hristian
