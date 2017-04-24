package fr.botai.rafkaf.api;

import org.springframework.web.client.RestTemplate;

public class TradeCall {

	RestTemplate restTemplate;
	
	public TradeCall(){
		this.restTemplate = new RestTemplate();
	}
	
	public void callApi(/*String Url*/){
		System.out.println(restTemplate.getForObject("http://rates.fxcm.com/RatesXML", String.class));
	}
	
	public static void main(String[] args){
		new TradeCall().callApi();
	}
}
