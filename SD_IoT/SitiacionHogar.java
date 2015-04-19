package situaciones;

public class SituacionHogar {
	private String hogar; 
	private String localizacion; 
	private float latitud; 
	private float longitud;
	private String sensor;
	private String tiempoRegistro; 
	private float sensor_Luz;
	private String sensor_Mov;
	private float sensor_Temp; // temperatura interior
	
	public SituacionHogar(String ho, String l, float la, float lo,String s, String t, 
			float luz, String mov, float te) {
		hogar = ho;  
		localizacion = l; 
		latitud = la; 
		longitud = lo; 
		sensor = s;
		tiempoRegistro = t; 
		sensor_Luz = luz; 
		sensor_Mov = mov;
		sensor_Temp = te; 
	}
		
	public SituacionHogar() {
		
	}

	public String getHogar() {
		return hogar;
	}
	
	public String getSensor(){
		return sensor;
	}

	public String getLocalizacion() {
		return localizacion;
	}

	public float getLatitud() {
		return latitud;
	}

	public float getLongitud() {
		return longitud;
	}

	public float getSensorTemp() {
		return sensor_Temp;
	}

	public float getSensorLuz() {
		return sensor_Luz;
	}

	public String getSensorMov() {
		return sensor_Mov;
	}

	
	public void setHogar(String ho) {
		hogar = ho;
	}
	
	public void setSensor(String s){
		sensor = s;
	}

	public void setLocalizacion(String l) {
		localizacion = l; 
	}

	public void setLatitud(float la) {
		latitud = la; 
	}

	public void setLongitud(float lo) {
		longitud = lo; 
	}

	public void setTiempoRegistro(String t) {
		tiempoRegistro = t; 
	}

	public void setSensorTemp(float te) {
		sensor_Temp = te; 
	}

	public void setSensorLuz(float luz) {
		sensor_Luz = luz; 
	}

	public void setSensorMov(String mov) {
			sensor_Mov = mov;
	}


	@Override
	public String toString() {
		
		return "Situacion:\n"
				+"\ntiempoRegistro= " + tiempoRegistro
				+ "\nTemperatura= " + sensor_Temp + "\nLuminosidad= " + sensor_Luz
				+ "\nIntrusion= " + sensor_Mov;
	}

}
