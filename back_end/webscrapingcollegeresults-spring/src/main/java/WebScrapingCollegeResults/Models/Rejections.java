package WebScrapingCollegeResults.Models;
import jakarta.persistence.*;

import java.lang.reflect.Array;
import java.util.ArrayList;

@Entity
@Table(name = "rejections")
public class Rejections {

    @Id
    @Column(name = "id")
    private int ID;

    @Column(name = "rejectlist")
    private ArrayList<String> rejectList;

    @ManyToOne
    @JoinColumn(name = "\"Attributeid\"", referencedColumnName = "timestamp") // Adjusted to reference the foreign key column
    private Attributes attributeID;



}

