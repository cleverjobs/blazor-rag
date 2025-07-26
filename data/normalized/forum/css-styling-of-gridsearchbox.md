# CSS Styling of GridSearchBox

## Question

**RobRob** asked on 26 Jan 2023

I'm looking to change the selected styling of the grid search box. When currently selected it is set as blue (using the theme I'm using). I have set up a css class and referenced it from the search box itself. What I don't understand is how to change the selected border styling colour of the search box. This is what I have thus far: .gridsearchbox { height: 24px; margin-right: 4px!important; font-size: 12px!important;
} I just want to set the selected border colour to for example red. Many thanks, Rob

## Answer

**Radko** answered on 27 Jan 2023

Hi Rob, The blue styling you are referring to is a box-shadow property, applied on the searchbox element, through a:focus-within pseudo selector. To change it, you can use a selector similar to the following: .gridsearchbox.k-input-solid:focus -within { box-shadow: 0 0 0 0.25rem red;
} I have also prepared a REPL example for you to test directly: [https://blazorrepl.telerik.com/Qxkvcrlv547aHjjK44](https://blazorrepl.telerik.com/Qxkvcrlv547aHjjK44) Hope the above helps. Regards, Radko Stanev

### Response

**Rob** commented on 27 Jan 2023

Hi Radko, Excellent. Have looked at the REPL; have implemented your suggestion and it's exactly what I was after. Many thanks! Rob
