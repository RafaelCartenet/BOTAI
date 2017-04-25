package fr.botai.rafkaf.api;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.springframework.web.client.RestTemplate;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

import fr.botai.rafkaf.model.XmlTreatment;
import fr.botai.rafkaf.model.Rate;

public class TradeCall {

	RestTemplate restTemplate;
	
	public TradeCall(){
		this.restTemplate = new RestTemplate();
	}
	
	public List<Rate> callApiSpecific(){
		try{	
			String pre_apiURL = "https://rates.fxcm.com/RatesXML";        
			URLConnection  url = new URL(pre_apiURL).openConnection();
			url.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11");
			url.connect();
			
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();	
			DocumentBuilder db = dbf.newDocumentBuilder();
			BufferedReader r  = new BufferedReader(new InputStreamReader(url.getInputStream(),Charset.forName("UTF-8")));
			StringBuilder sb = new StringBuilder();
			String line;
			while ((line = r.readLine()) != null) {
			    sb.append(line);
			}
			
			Document doc = db.parse(new InputSource(new StringReader(sb.toString())));
			doc.normalize();
			
			doc = XmlTreatment.stripEmptyNode(doc);
			return XmlTreatment.parseRatesXML(doc.getChildNodes().item(0).getChildNodes());
		}catch(Exception e){
			System.out.println(e);
			return new ArrayList<>();
		}		
	}
	
}
