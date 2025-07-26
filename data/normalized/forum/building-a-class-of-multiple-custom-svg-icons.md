# Building a class of multiple custom SVG icons

## Question

**Dav** asked on 26 Jul 2023

In the documentation on the SVG Icon component here, one icon is defined in the following code: public class Moon: SvgIconBase { public Moon () {
Name="moon";
Content="<path d=\"M8.85028 16.5C11.3178 16.5 13.5715 15.3773 15.0646 13.5378C15.2854 13.2656 15.0446 12.8681 14.7032 12.9331C10.8219 13.6723 7.25756 10.6963 7.25756 6.77825C7.25756 4.52131 8.46575 2.44591 10.4294 1.32844C10.7321 1.15619 10.6559 0.697281 10.312 0.63375C9.82984 0.544842 9.34057 0.500073 8.85028 0.5C4.43437 0.5 0.850281 4.07847 0.850281 8.5C0.850281 12.9159 4.42875 16.5 8.85028 16.5Z\" fill=\"rgb(31, 31, 31)\" />";
ViewBox="0 0 16 17";
}
} public static class MySvgIcons { public static ISvgIcon Moon=> new Moon(); //public static ISvgIcon AnotherIcon=> new AnotherIcon(); } In this snippet, an example is provided to add another icon to the MySvgIcons class, but where should that icon be defined? It seems impractical to replicate the entire first class structure for each and every icon. Is there a more efficient way of loading SVGs into my custom class of icons?

## Answer

**Radko** answered on 28 Jul 2023

Hi David, The approach from our documentation that you have outlined is valid only when you would like to provide a custom icon to the Icon parameter of an existing component. In other words, if you would like to simply render a custom SVG icon, then you can render the SVG markup directly in your razor file. As for a recommended approach - this is more or less what we are doing in the Telerik.SvgIcons package. Its source code can be found here: [https://github.com/telerik/kendo-icons/tree/develop/packages/svg-icons/src-cs/Telerik.SvgIcons.](https://github.com/telerik/kendo-icons/tree/develop/packages/svg-icons/src-cs/Telerik.SvgIcons.) However, when it comes to your own custom icons, you do not have to follow the exact same pattern, and as long as you pass the necessary props and inherit SvgIconBase, you should be able to use them in our components. Regards, Radko Progress Telerik
