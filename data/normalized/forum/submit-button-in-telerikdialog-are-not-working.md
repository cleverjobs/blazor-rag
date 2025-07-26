# Submit button in TelerikDialog are not working

## Question

**Mar** asked on 13 Mar 2023

I have the following buttons When I press enter nothing happens <DialogButtons> <TelerikButton OnClick=" @( ()=> { IsModalVisible=false; } ) "> Cancel </TelerikButton> <TelerikButton OnClick=" @( ()=> { IsModalVisible=false; CreateTrade (); } ) " ButtonType="ButtonType. Submit " ThemeColor=" @ThemeConstants.Button.ThemeColor. Primary "> Create Trade </TelerikButton> </DialogButtons>

## Answer

**Dimo** answered on 14 Mar 2023

Hi Martin, It looks like you want to submit a form. However, these Dialog buttons are not rendered inside a form. That's why Enter keypress has no effect. Use the Id parameter of the form and the Form parameter of the Submit button to define a relationship between the two components. You will also need to close the Dialog explicitly on form submit. If there is no Form in this scenario, then Enter keypress will work only if you focus any of the two buttons, or if you implement a custom @keydown handler for a container inside the Dialog content. Regards, Dimo Progress Telerik

### Response

**Karl** commented on 05 Apr 2024

As Dimo suggested, the Dialog contents are hoisted to the root element, TelerikForms seem to only look within content rendered inside of their tags for a button of type Submit. Dimo's suggestion allows you to create a relationship between Dialog buttons, and a form... but this relationship can only go one-way. Setting an Id on the TelerikForm, and setting the Form attribute on a Dialog button with Type Submit will allow that button to trigger the TelerikForm's OnSubmit or OnValidSubmit. If you pursue that route, I would encourage you to remove an onClickHandler from the DialogButtons... something a little like this: <TelerikDialog...> <DialogTitle> This is a form in a Dialog! </DialogTitle> <DialogContent> <TelerikForm Id="MyForm" OnSubmit="@(()=> { IsModalVisible=false; CreateTrade();})"...> </TelerikForm> </DialogContent> <DialogButtons> <TelerikButton OnClick="@(()=> { IsModalVisible=false; })"> Cancel </TelerikButton> <TelerikButton ButtonType="ButtonType.Submit" Form="MyForm"> Submit </TelerikButton> </DialogButtons> </TelerikDialog> The problem... is that this just makes the button "submit the form" and run form validation... this doesn't allow enter to "submit the form". Focusing the submit button, and pressing enter or Space would now trigger the form submit action... but the original ask is still on the table as something that Telerik can't easily do. As Dimo said, you are still able to write an entire @keydown handler to make do... but it's a shame when there's default browser form behavior being left on the table like this. I'm in the same boat myself. I'm considering rendering a non-visible button (yuck) in my TelerikForm and setting the Form attritbute on THAT button to also trigger the form submit behavior. <TelerikDialog...> <DialogTitle> This is a form in a Dialog! </DialogTitle> <DialogContent> <TelerikForm Id="MyForm" OnSubmit="@(()=> { IsModalVisible=false; CreateTrade();})"...> <FormItemsTemplate> <TelerikButton Class="!k-display-none" ButtonType="ButtonType.Submit" Form="MyForm"> Yucky Invisible Button </TelerikButton> </FormItemsTemplate> <FormButtons /> </TelerikForm> </DialogContent> <DialogButtons> <TelerikButton OnClick="@(()=> { IsModalVisible=false; })"> Cancel </TelerikButton> <TelerikButton ButtonType="ButtonType.Submit" Form="MyForm"> Submit </TelerikButton> </DialogButtons> </TelerikDialog> However... when I tried this... I noticed that I couldn't use the <FormButton/> render fragment and I HAD to insert the display:none button in my form's content... first thing... There's something funky goin' on.

### Response

**Dimo** commented on 08 Apr 2024

@Karl On one hand, I don't see a reason to use Dialog action buttons to submit a Form that is already inside the Dialog. Why not use buttons inside the Form and spare the hassle? On the other hand, my observations do not match your statements - I can submit the Form with a hidden Button inside <FormButtons> just fine: [https://blazorrepl.telerik.com/wSaokslx04KeTV2l36](https://blazorrepl.telerik.com/wSaokslx04KeTV2l36)

### Response

**Karl** commented on 18 Apr 2024

If stuffing an invisible button into the form buttons template works, I think that's the best compromise so far! I could have made a syntax error in my razor template when I tried... but my initial attempts using the form button template seemed to have trouble. I couldn't get my solution to work if my invisible button was in the form buttons template, or at the end of the form... I had to hoist it to be the first thing in my form items template. Something may be awry in our implementation as well, I'm not claiming to be perfect here. I do like your question: "Well if having a button in the form works, then why have dialog buttons at all? Just fill out the FormButtons template!" My answer is: "I need other dialog controls" The designer on our team would like to see a couple of context actions in the bottom of the dialog. Cancel, Submit, and some application specific extras, etc. If the controls for the cancel & extra actions show up in the <DialogButtons> template... I would _also_ like my form's submit button to share that layout. Moving all buttons into the form's <FormButtons> template starts to tightly couple Submit (which is fine) as well as Dialog specific controls and behavior to our custom component that wraps a TelerikForm (less fine) If we move every button that was previously in the dialog into the Form's FormButtons template, we'd need to drill several events with a needless amount of boilerplate. Moving ONLY the submit button into the <FormButtons> template while leaving the others in the <DialogButtons> separates the buttons into different layouts visually and creates a headache that's not worth solving. In my opinion, only having one extra yucky invisible button is the best compromise so far... wherever it works.
