# Notification Area

## Question

**Geo** asked on 04 Dec 2020

I would be nice if the Notification component would just render in the location where it was put by default. Very strange that it doesn't.

## Answer

**Nadezhda Tacheva** answered on 08 Dec 2020

Hi George, The Notification component is generally displayed in its place of declaration. However, all the Notifications instances are wrapped in a container and we have styled it to be displayed in a different position for design purposes (it has position: fixed). I'm attaching an example project showing that the Notifications position can be modified to appear where it was put by default by setting the container class position to static (see MainLayout.razor file for reference). The project is also an example of implementing only one Notification Instance for all Components which can be a very useful approach in certain scenarios. Regards, Nadezhda
