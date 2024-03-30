package WebScrapingCollegeResults;

import WebScrapingCollegeResults.Models.*;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.criteria.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.*;

@RestController
public class ApplicationsController {

    @PersistenceContext
    private EntityManager entityManager;
    @GetMapping("api/Gender")
    public ResponseEntity<Map<Long, String>> getGender() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Attributes> root = query.from(Attributes.class);
        query.multiselect(root.get("timestamp"), root.get("Gender"));
        List<Object[]> results = entityManager.createQuery(query).getResultList();

        Map<Long, String> genderMap = new HashMap<>();
        for (Object[] result : results) {
            genderMap.put((Long) result[0], (String) result[1]);
        }
        return new ResponseEntity<>(genderMap, HttpStatus.OK);
    }

    @GetMapping("api/SAT")
    public ResponseEntity<Map<Long, String>> getSAT() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Attributes> root = query.from(Attributes.class);
        query.multiselect(root.get("timestamp"), root.get("SAT"));
        List<Object[]> results = entityManager.createQuery(query).getResultList();

        Map<Long, String> satMap = new HashMap<>();
        for (Object[] result : results) {
            satMap.put((Long) result[0], (String) result[1]);
        }
        return new ResponseEntity<>(satMap, HttpStatus.OK);
    }

    @GetMapping("api/ACT")
    public ResponseEntity<Map<Long, String>> getACT() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Attributes> root = query.from(Attributes.class);
        query.multiselect(root.get("timestamp"), root.get("ACT"));
        List<Object[]> results = entityManager.createQuery(query).getResultList();

        Map<Long, String> actMap = new HashMap<>();
        for (Object[] result : results) {
            actMap.put((Long) result[0], (String) result[1]);
        }
        return new ResponseEntity<>(actMap, HttpStatus.OK);
    }

    @GetMapping("api/URL")
    public ResponseEntity<Map<Long, String>> getURL() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Attributes> root = query.from(Attributes.class);
        query.multiselect(root.get("timestamp"), root.get("URL"));
        List<Object[]> results = entityManager.createQuery(query).getResultList();

        Map<Long, String> urlMap = new HashMap<>();
        for (Object[] result : results) {
            urlMap.put((Long) result[0], (String) result[1]);
        }
        return new ResponseEntity<>(urlMap, HttpStatus.OK);
    }

    @GetMapping("api/Major")
    public ResponseEntity<Map<Long, List<String>>> getMajor() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Major> root = query.from(Major.class);

        // Grouping by attributeID and concatenating majorlist
        query.multiselect(
                root.get("attributeID").get("timestamp"),
                cb.function("string_agg", String.class, root.get("majorList"), cb.literal(", "))
        ).groupBy(root.get("attributeID"));

        List<Object[]> results = entityManager.createQuery(query).getResultList();

        // Convert the result to a dictionary
        Map<Long, List<String>> resultDict = new HashMap<>();
        for (Object[] result : results) {
            Long attributeId = (Long) result[0];
            String majorlist = (String) result[1];
            resultDict.put(attributeId, List.of(majorlist.split(", ")));
        }

        return new ResponseEntity<>(resultDict, HttpStatus.OK);
    }

    @GetMapping("api/Acceptances")
    public ResponseEntity<Map<Long, List<String>>> getAcceptances() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Acceptances> root = query.from(Acceptances.class);

        query.multiselect(
                root.get("attributeID").get("timestamp"),
                cb.function("string_agg", String.class, root.get("acceptList"), cb.literal(", "))
        ).groupBy(root.get("attributeID"));

        List<Object[]> results = entityManager.createQuery(query).getResultList();

        // Convert the result to a dictionary
        Map<Long, List<String>> resultDict = new HashMap<>();
        for (Object[] result : results) {
            Long attributeId = (Long) result[0];
            String acceptlist = (String) result[1];
            resultDict.put(attributeId, List.of(acceptlist.split(", ")));
        }

        return new ResponseEntity<>(resultDict, HttpStatus.OK);
    }

    @GetMapping("api/Rejections")
    public ResponseEntity<Map<Long, List<String>>> getRejections() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Rejections> root = query.from(Rejections.class);

        query.multiselect(
                root.get("attributeID").get("timestamp"),
                cb.function("string_agg", String.class, root.get("rejectList"), cb.literal(", "))
        ).groupBy(root.get("attributeID"));

        List<Object[]> results = entityManager.createQuery(query).getResultList();

        // Convert the result to a dictionary
        Map<Long, List<String>> resultDict = new HashMap<>();
        for (Object[] result : results) {
            Long attributeId = (Long) result[0];
            String rejectList = (String) result[1];
            resultDict.put(attributeId, List.of(rejectList.split(", ")));
        }

        return new ResponseEntity<>(resultDict, HttpStatus.OK);
    }

    @GetMapping("api/Extracurriculars")
    public ResponseEntity<Map<Long, List<String>>> getExtracurriculars() {
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Object[]> query = cb.createQuery(Object[].class);
        Root<Extracurriculars> root = query.from(Extracurriculars.class);

        query.multiselect(
                root.get("attributeID").get("timestamp"),
                cb.function("string_agg", String.class, root.get("ecsList"), cb.literal(", "))
        ).groupBy(root.get("attributeID"));

        List<Object[]> results = entityManager.createQuery(query).getResultList();

        // Convert the result to a dictionary
        Map<Long, List<String>> resultDict = new HashMap<>();
        for (Object[] result : results) {
            Long attributeId = (Long) result[0];
            String ecsList = (String) result[1];
            resultDict.put(attributeId, List.of(ecsList.split(", ")));
        }

        return new ResponseEntity<>(resultDict, HttpStatus.OK);
    }

    @PostMapping("api/Gender")
    Public boolean postGender()



}
