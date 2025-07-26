# Styling Command Button's

## Question

**RobRob** asked on 09 Apr 2020

Is there a way to apply more styles to the GridCommandButton's? I would like the icons and labels to be differentiated a little more like the following... [https://codepen.io/danielmariveles/pen/jPrwxv](https://codepen.io/danielmariveles/pen/jPrwxv) Thanks, Rob

## Answer

**Marin Bratanov** answered on 09 Apr 2020

Hi Rob, You can add content between the opening and closing tags of the command button in order to add custom icons (in case the built-in ones don't suffice). You can also add a Class to the button to add the desired styling that will override the built-in styles we have. An alternative is to use a regular column to put your own buttons and control the grid through its state, as explained here: [https://feedback.telerik.com/blazor/1461283-pass-the-model-context-to-command-button.](https://feedback.telerik.com/blazor/1461283-pass-the-model-context-to-command-button.) Regards, Marin Bratanov
