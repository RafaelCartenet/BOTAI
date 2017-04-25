package fr.botai.rafkaf.api;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import fr.botai.rafkaf.model.Rate;
import fr.botai.rafkaf.repository.RateRepository;

@Service
public class RateService {
	
	@Autowired
	private RateRepository rateRepository;
	
	public List<Rate> findAll(){
		List<Rate> list = new ArrayList<>();
		rateRepository.findAll().forEach(list::add);
		return list;
	}

	public boolean saveList(List<Rate> rates){
		try{
			rates.forEach(rateRepository::save);
			return true;
		}catch(Exception e){
			System.out.println(e);
			return false;
		}
	}
	
}
