# Alternating Grid Row Color when Using Small Grid Size Theme

## Question

**Lel** asked on 20 Mar 2024

My project's Theme Builder is set up to show an alternating color for the TelerikGrid rows. However, if I use a compact grid through Grid Sizing by setting Size="@ThemeConstants.Grid.Size.Small", the alternating row color disappears. How can I get the alternating rows when using the Small Grid Theme?

## Answer

**Dimo** answered on 21 Mar 2024

Hello Leland, The Grid should show alternating row backgrounds no matter the Size. You can see this in action in the example in our Grid Size documentation. Please make sure that the custom theme in the app is up-to-date. For example, you may need to migrate your ThemeBuilder theme project. If necessary, please send an isolated runnable example for inspection. Regards, Dimo Progress Telerik
