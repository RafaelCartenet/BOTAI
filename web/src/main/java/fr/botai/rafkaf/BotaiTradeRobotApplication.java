package fr.botai.rafkaf;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
@EnableScheduling
public class BotaiTradeRobotApplication {

	public static void main(String[] args) {
		RestTemplate restTemplate = new RestTemplate();
		SpringApplication.run(BotaiTradeRobotApplication.class, args);
		
	}
	
}
