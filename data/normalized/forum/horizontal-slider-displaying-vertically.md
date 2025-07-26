# Horizontal slider displaying vertically

## Question

**Edd** asked on 09 Mar 2022

I am using the radslider and have it oriented horizontally but it displays vertically. I attached a screenshot below. <div class="column is-half"> <small>Weeks ahead to buy</small><br /> <strong><TelerikSlider @bind-Value="@Value" Min="0" Max="6" SmallStep="1" LargeStep="2" Width="350px" Orientation="SliderOrientation.Horizontal"> </TelerikSlider></strong> </div>

### Response

**Marin Bratanov** commented on 12 Mar 2022

Double check that you are referencing the correct Telerik stylesheet (see more here ) and try removing custom CSS from the page/project - there may be some generic rule that affects the slider as well (say, some flexbox setting).
