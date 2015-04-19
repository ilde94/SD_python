package situaciones;

import org.mule.api.annotations.ContainsTransformerMethods;
import org.mule.api.annotations.Transformer;
import org.mule.module.json.JsonData;

import situaciones.SituacionHogar;

// ver http://www.mulesoft.org/docs/site/current3/apidocs/org/mule/module/json/JsonData.html


@ContainsTransformerMethods
public class Transformador
{
	@Transformer  
	public SituacionHogar JSONToSituacionHogar(JsonData obj) throws Exception 
	{	  	  
		SituacionHogar evento = new SituacionHogar();
		String nombreHogar = obj.getAsString("channel/name");
		
		evento.setHogar(nombreHogar);
		evento.setSensor(obj.getAsString("channel/description")); 
		evento.setLocalizacion(obj.getAsString("channel/name"));
		evento.setLatitud(Float.parseFloat(obj.getAsString("channel/latitude")));
		evento.setLongitud(Float.parseFloat(obj.getAsString("channel/longitude")));
		evento.setTiempoRegistro(obj.getAsString("channel/updated_at"));
		
		if(nombreHogar.equalsIgnoreCase("IoT_SD_David_Ilde")) 
		{
			evento.setSensorTemp(Float.parseFloat(obj.getAsString("feeds[1]/field1")));
			evento.setSensorLuz(Float.parseFloat(obj.getAsString("feeds[1]/field2")));
			evento.setSensorMov(obj.getAsString("feeds[1]/field3"));
		}
		else 
		{
			System.out.println("No es posible realizar la conversión");
		}
			
		System.out.println("Mensaje de CasaDomotica:\n" + evento); 
		
		return evento; 
	}
}

