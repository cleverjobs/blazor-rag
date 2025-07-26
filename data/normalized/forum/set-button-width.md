# Set button width

## Question

**Joe** asked on 22 May 2025

How do I tell the button to fill the available width? I'd like this to be as wide as the other controls and it should adapt to width changes of the page. I have this definition: As a bonus, the only way I can get the button to align to the bottom is to put in the white label. My attempts at aligning to the bottom have failed. <TelerikCard Width="25vh"> <CardBody> <div class="form-group-short"> <label class="col-form-label"> Patient Status </label> <br /> <TelerikDropDownList @bind-Value="@IsActiveFilterIndex" TextField="Name" ValueField="Id" ReadOnly="@(!IsActiveFilterEnabled)" Data="@IsActiveFilterOptions"> </TelerikDropDownList> </div> <div class="form-group-short align-bottom"> <label class="col-form-label gsi-color-white"> Apply Filter </label> <br /> <TelerikButton OnClick="OnFilter" Class="gsi-background-color gsi-color-white"> Apply Filter </TelerikButton> </div> </CardBody> </TelerikCard>

## Answer

**Justin** answered on 23 May 2025

Hi Joel, To set the width of the button to take up the same amount of space in the card that the other controls do, and also change dynamically based on the size of the container, you can apply a custom CSS class directly to the button. In this custom CSS class, set the width attribute to 100%. Like this: <TelerikButton Class="customWidth"> TelerikButton </TelerikButton> <style>.customWidth { width: 100%; </style> The general approach is described in Button Class. I hope this helps. Regards, Justin Progress Telerik

### Response

**Joel** commented on 27 May 2025

Thanks for this. For some reason, it didn't apply this change until I marked it with !Important. That got me there. .gsi-width-100pct {
width: 100% !important;
} <div class="form-group-short align-bottom"> <label class="col-form-label gsi-color-white"> Apply Filter </label> <br /> <TelerikButton OnClick="OnFilter" Class="gsi-background-color gsi-color-white gsi-width-100pct"> Apply Filter </TelerikButton> </div>
