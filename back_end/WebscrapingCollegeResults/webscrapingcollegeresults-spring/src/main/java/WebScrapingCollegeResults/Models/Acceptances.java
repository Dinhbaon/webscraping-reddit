package WebScrapingCollegeResults.Models;
import jakarta.persistence.*;

import java.lang.reflect.Array;
import java.util.ArrayList;

@Entity
@Table(name = "acceptances")
public class Acceptances {

    @Id
    @Column(name = "id")
    private int ID;

    @Column(name = "acceptlist")
    private ArrayList<String> acceptList;

    @ManyToOne
    @JoinColumn(name = "\"Attributeid\"", referencedColumnName = "timestamp") // Adjusted to reference the foreign key column
    private Attributes attributeID;



}

