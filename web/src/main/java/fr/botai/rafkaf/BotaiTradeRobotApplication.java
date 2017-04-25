package fr.botai.rafkaf;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class BotaiTradeRobotApplication {

	public static void main(String[] args) {
		SpringApplication.run(BotaiTradeRobotApplication.class, args);	
	}
	
}
