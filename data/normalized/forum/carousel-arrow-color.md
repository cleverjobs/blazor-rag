# Carousel arrow color

## Question

**Dea** asked on 11 Jul 2025

Sorry I'm sure I've missed this somewhere obvious, but how can I set the color of the arrows on a Carousel, so that they are visible against a white background?

## Answer

**Hristian Stefanov** answered on 11 Jul 2025

Hi Dean, You can easily change the Carousel's arrows color by using the following CSS selectors: <TelerikCarousel Data="@CarouselData" Width="400px" Height="200px"> <Template> <div class="item"> ID @(context.ID) : @(context.Text) </div> </Template> </TelerikCarousel> <style>.k-scrollview-next.k-svg-i-chevron-right,.k-scrollview-prev.k-svg-i-chevron-left { color: red;
} </style> <style>.item { background: #3d57d8; color: #fff; font: 36px / 200px sans-serif; text-align: center;
} </style> @code {
public IEnumerable <CarouselModel> CarouselData=Enumerable.Range(1, 5).Select(x=> new CarouselModel
{
ID=x,
Text="Text " + x
});

public class CarouselModel
{
public int ID { get; set; }
public string Text { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Dean** commented on 11 Jul 2025

Perfect thanks - could you point me to the reference for this please? I'd also like to style the active/inactive page icons, and style an arrow differently if there are no more items in that direction, if possible.

### Response

**Hristian Stefanov** commented on 14 Jul 2025

Hi Dean, You can use custom CSS to override specific styles for individual components. Inspect the rendered HTML using browser developer tools to identify the classes and elements you want to style differently. Then, create custom CSS rules to apply your desired styles. Best, Hristian
