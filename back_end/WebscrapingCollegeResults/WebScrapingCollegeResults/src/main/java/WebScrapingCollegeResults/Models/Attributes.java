package WebScrapingCollegeResults.Models;


import jakarta.persistence.*;

import java.io.Serializable;
import java.util.Set;

@Entity
@Table(name = "attributes", schema = "public")
public class Attributes implements Serializable {

    @Id

    @Column(name = "timestamp")
    private Long timestamp;

    @Column(name = "\"Gender\"") // Adjusted to match the case in the database
    private String Gender;    // Adjusted to match the case in the database

    @Column(name = "\"SAT\"")
    private String SAT;

    @Column(name = "\"ACT\"")
    private String ACT;

    @Column(name = "\"URL\"")
    private String URL;

    public Attributes(Long timestamp, String gender, String sat, String act, String url) {
        this.timestamp = timestamp;
        this.Gender = gender;
        this.SAT = sat;
        this.ACT = act;
        this.URL = url;
    }
    @OneToMany(mappedBy = "attributeID")
    private Set<Major> majors;

}
