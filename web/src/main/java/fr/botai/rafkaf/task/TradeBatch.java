package fr.botai.rafkaf.task;

import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class TradeBatch {

	private Logger logger = LoggerFactory.getLogger(this.getClass());

	@Scheduled(
			cron= "0,30 * * * * *"
			)
	public void cronJob(){
		logger.info("-> cron Job beginning at" + new Date().getTime());
		
		logger.info("-> cron Job" + + new Date().getTime());
	}

}
