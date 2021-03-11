# Belle Pan 260839939
# COMP 204 - Assignment 3


# DO NOT EDIT THIS FUNCTION. USE IT TO SORT LISTS OF TUPLES
def get_key1(item):
    """
    Args:
        A tuple of 2 objects, where the second is an integer
    returns:
        The value of the second member of the tuple, 
        plus a value between 0 and 0.01 obtained from the first
        member of the tuple. This second term is only useful
        to break ties in a deterministic manner. This is a detail
        you can afford to ignore.
    """
    return item[1]+float(hash(item[0])%1000000000)/100000000000

# DO NOT EDIT THIS FUNCTION.
def read_data_from_file(filename):
    """
    args:
        filename: Name of file containing medical data
    Returns:
        Tuple of a dictionary of symptoms and a dictionary of diagnostics
    """
    
    f = open(filename,'r')
    lines = f.read().splitlines()
    
    i =0
    symptoms_by_patient={}
    diagnostic_by_patient={}
    l=len(lines)
    while i<l:
        ID=int(lines[i].split()[0])
        present = set(lines[i+1].split())
        absent = set(lines[i+2].split())
        diag = lines[i+3].split()[0]
        symptoms_by_patient[ID]=(present,absent)
        diagnostic_by_patient[ID]=diag
        i += 4
        
    return symptoms_by_patient, diagnostic_by_patient



def symptom_similarity(symptoms_tuple_A, symptoms_tuple_B):
    """
    Args:
        symptoms1: tuple of a set of symptoms present and a set of symptoms absent
        symptoms2: tuple of a set of symptoms present and a set symptoms absent
    Returns:
        present_present + absent_absent - present_absent - absent_present
        where common_present is the number of symptoms present in both patients
        absent_absent is the number of symptoms absent in both patients
        present_absent is the number of symptoms present in patientA and absent          
        in patientB
        absent_present is the number of symptoms absent in patientA and present         
        in patientB
    """
    common_present = len(symptoms_tuple_A[0].intersection(symptoms_tuple_B[0]))
    #identifies number of symptoms that are present in patientA and finds symptoms common to both patients
    absent_absent = len(symptoms_tuple_A[1].intersection(symptoms_tuple_B[1]))
    #identifies number of symptoms that are not present in both patients
    present_absent = len(symptoms_tuple_A[0].intersection(symptoms_tuple_B[1]))
    #identifies number of symptoms present in patient A, but not in patient B
    absent_present = len(symptoms_tuple_A[1].intersection(symptoms_tuple_B[0]))
    #identifies number of symptoms present in patient B, but not in patient A
    return(common_present + absent_absent - present_absent - absent_present)
    #returns the similarity between two patients represented by a numerical value


def similarity_to_patients(my_symptoms, all_patients):
    """
    Args:
        my_symptoms: tuple of symptoms present and absent
        all_patients: dictionary of patients IDs (key) and associated tuple of
                      present and absent symptoms
    Returns:
        List of tuples. Each tuple is of the form: (patientID, similarity), 
        with one tuple per patient in all_patients. 
        For each patient in all_patients, similarity is the symptom similarity 
        between my_symptoms and the patient’s symptoms. The list should be 
        sorted in decreasing order of similarity.
     """
    similarity_list = []
    #an empty list to store the tuples of patientID and symptom similarity
    for patient in all_patients: 
        #iterates through all the patients (keys) of all_patients to isolate and compare similarities with my_symptoms
        patient_symptoms = all_patients[patient]
        #gives the symptoms that a patient exhibits (values)
        similarity_list.append((patient, symptom_similarity(my_symptoms, patient_symptoms)))
        #appends a tuple to similarity_list with the patientID and symptom similarity
    similarity_list.sort(key = lambda tup:(tup[1],tup[0]), reverse = True)
    #sort similarity_list in decreasing order by the second element in the tuple through utilizing key=lambda tup[1], then by its first element via tup[0]
    return(similarity_list)
       
   

def most_similar_patients(my_symptoms, all_patients, n_top):
    """
    Args:
        my_symptoms: tuple of a set of symptoms present and absent
        all_patients: dictionary of patients IDs (key) and associated tuple of
                      present and absent symptoms
        n_top: Maximum number of patients to return
    Returns:
        The set of up to n_top patient IDs from all_patients 
        with the highest similarity to my_symptoms
    """ 
#    similarity_to_patients(my_symptoms, all_patients)
    patient_list = similarity_to_patients(my_symptoms, all_patients)
    #creates list of tuples of patientID and similarity, includes all patients
    set_patientID = {patient_list[patient][0] for patient in range (0, (n_top))}
    #assembles a set of patientIDs from patients_list within the identified range
    return(set_patientID)
    
    
    
def count_diagnostics(patient_set, diagnostic_by_patient):
    """
    Args:
        patient_set: A set of patient IDs
        diagnostic_by_patient: A dictionary with key = patient_ID and values = diseases
    Returns:
        A dictionary with keys = diagnostic and 
        values = fraction of patients in patient_set with that diagnostic
    """     
    diagnostic_dict = {}
    #creates empty dictionary
    for patientID in diagnostic_by_patient:
    #iterates through keys (patient) and values (disease) in diagnostic_by_patient dictionary
        disease = diagnostic_by_patient[patientID]
        #stores the value of key (patientID) in variable disease
        for patient in patient_set:
        #iterates through patients in patient_set (used for later)
            if patient == patientID:
                if disease not in diagnostic_dict:
                    diagnostic_dict[disease] = (1.0/len(patient_set))
                else:
                    diagnostic_dict[disease] += (1.0/len(patient_set))
                #if disease is not already in the dictionary diagnostic_dict,
                #adds new key (disease) and value of 0 to the diagnostic_dict dictionary
                #if patient in patient_set is present in diagnostic_by_patient, 
                #the value for disease in diagnostic_dict is upated by 1 in number of patients in patient_set 
    return diagnostic_dict
    


def diagnostics_from_symptoms(my_symptoms, all_patients_symptoms, all_patients_diagnostics, n_top):
    """
    Args:
        my_symptoms: tuple of symptoms present and absent
        all_patients_symptoms: dictionary of patients IDs (key) and associated symptoms
        all_patients_diagnostics: dictionary of patients IDs (key) and associated diagnostic
        n_top: Number of most similar patients to consider.
    Returns:
        A dictionary with keys = diagnostic and 
        values = fraction of the n_top most similar patients with that diagnostic
    """
    patient_set = most_similar_patients(my_symptoms, all_patients_symptoms, n_top)
    #calls most_similar_patients function and stores the return (set of patientID's) in variable patient_set
    diagnostic_freq = count_diagnostics(patient_set, all_patients_diagnostics)
    return (diagnostic_freq)
    #calls and returns the count_diagnostics function which returns a dictionary with keys = diagnostic and 
    #values = fraction of patients in patient_set with that diagnostic
    
  


def pretty_print_diagnostics(diagnostic_freq):
    """
    Args:
        diagnostic_freq: A dictionary with key = diagnostic and value = frequency
    Returns:
        Nothing
    Prints:
        A table of possible diagnostics, sorted by frequency, expressed as percentages. 
        Only diagnostics with non-zero percentages should be printed.
        If a diagnostic is longer than 10 characters, it should be truncated to 10 characters.
        Frequencies should be expressed as percentages, rounded to the nearest percent.
    """     
    pretty_dic = {}
    #creates empty dictionary pretty_dic
    for key, value in diagnostic_freq.items():
    #iterates through all diagnostics in diagnostic_freq
            pretty_dic[key] = round(value * 100)
            #adds a new key (diagnostic) assigned a value (diagnostic frequency) that is represented as a percentage
            #round() rounds the value to its nearest integer 
    for diagnostic, frequency in pretty_dic.items():
        print(f'{diagnostic:10.10} {str(frequency) + "%"}')
        #formats key of pretty_dic to 10 characters
        #converts value of pretty_dic to a string so as to concatenate it with "%"
 
    

def diagnostic_clarity(diagnostic_freq):
    """
    Args:
        diagnostic_freq: A dictionary with key = diagnostic and value = frequency
    Returns:
        The clarity of the diagnostic, defined at the frequency of the 
        most likely disease.
    """
    clarity = 0
    for key, frequency in diagnostic_freq.items():
        if frequency >= clarity:
            clarity = frequency
        #finds the highest frquency of the listed diagnostics and stores it in variable clarity        
    return clarity

    

def recommend_symptom_to_test(my_symptoms, all_patients_symptoms, all_patients_diagnostics, n_top):
    """
    Args:
        my_symptoms: tuple of symptoms present and absent
        all_patients_symptoms: dictionary of patients IDs (key) and associated symptoms
        all_patients_diagnostics: dictionary of patients IDs (key) and associated diagnostic
        n_top: Number of most similar patients to consider.
    Returns:
        A string describing the best symptom to test for in order to clarify the diagnostic.
    Explanation:
        The best symptom to test for is one that: 
        (i) has been tested at least once among the patients in all_patients_symptoms
        (ii) is not already in the new_patient_symptoms, and 
        (iii) yields the maximum value (see text of question for definition of value). 
    """
    x = 0
    s = "some symptom"
    #initializes the values x and s as variables for storage for the value of testing a particular symptom and the respective symptom with the highest score
    my_symptoms_pres_l = list(my_symptoms[0])
    my_symptoms_not_l = list(my_symptoms[1])
    #creates lists of symptoms present and not present in the patient of interest (important, as tuples are immutable and new symptoms cannot be added unless its type is modified)
    for patient,symptoms in all_patients_symptoms.items():
    #iterates through patients and their associated symptoms in the dictionary all_patients_symptoms
        for symptom_set in symptoms:
        #iterates through the sets of symptoms present and absent in symptoms of patients in all_patients_symptoms
            for symptom in symptom_set:
            #iterates through symptoms in symptom_set, ensures that the symptom of interest has been tested at least once among the patients in all_patients_symptoms
                if symptom not in my_symptoms_pres_l and symptom not in my_symptoms_not_l:
                #proceeds if the symptom of interest is not already present in my_symptoms and therefore has not been tested
                    new_symptoms = my_symptoms_pres_l + [symptom]
                    #adds new symptom to present symptoms for following hypothetical testing
                    new_symptoms_s = set(new_symptoms)
                    #creates a set out of the list of present symptoms
                    new1_my_symptoms = (new_symptoms_s,my_symptoms[1]) 
                    #creates new tuple of sets, with symptoms present (with additional symptom) and symptoms absent, replacing my_symptoms in following tests
                    diagnostic_freq1 = diagnostics_from_symptoms(new1_my_symptoms, all_patients_symptoms, all_patients_diagnostics, n_top)
                    #aqures diagnostic frequency of patient of interest if the symptom of interest was present
                
                    new_symptoms_not = my_symptoms_not_l + [symptom]
                    #adds new symptom to absent symptoms (for following hypothetical testing)
                    new_symptoms_not_s = set(new_symptoms_not)
                    #creates a set out of the list of absent symptoms
                    new2_my_symptoms = (my_symptoms[0], new_symptoms_not_s)
                    #creates new tuple of sets, with symptoms present and symptoms absent (with additional symptom), replacing my_symptoms in following tests
                    diagnostic_freq2 = diagnostics_from_symptoms(new2_my_symptoms, all_patients_symptoms, all_patients_diagnostics, n_top)
                    #aqures diagnostic frequency of patient of interest if the symptom of interest was absent
                    
                    value_x = 0.5*diagnostic_clarity(diagnostic_freq1) + 0.5*diagnostic_clarity(diagnostic_freq2)
                    #aquires value of testing for symptom of interest
                
                    if value_x > x:
                        x = value_x
                        s = symptom
                        #x and s update to the appropriate value if value_x is larger than previous tests
                        #ensures that the symptom returned yields the maximum value
    return s


def my_test():
    """ This function is used to test the other functions.
        Its expected output is contained in the file my_test_output.txt
        It will not be graded. We provided it to let you make sure
        that your own functions work properly.
    """
    
    # A small dictionary of patient's symptoms
    all_patients_symptoms = {56374: ({"headache","fever"}, {"coughing", "runny_nose","sneezing"}),
                           45437: ({"coughing", "runny_nose"},{"headache","fever"}),
                           16372: ({"coughing", "sore_throat"},{"fever"}),
                           54324: ({"vomiting", "coughing","stomach_pain"},{"fever"}),
                           35249: ({"sore_throat", "coughing","fever"},{"stomach_pain", "runny_nose"}),
                           44274: ({"fever", "headache"},{"stomach_pain", "runny_nose","sore_throat", "coughing",}), 
                           74821: ({"vomiting", "fever"},{"headache"}),
                           94231: ({"stomach_pain", "fever","sore_throat","coughing","headache"},{"vomiting"}),
                           }
    # A small dictionary of patient's diagnostics                  
    all_patients_diagnostics = {45437: "cold", 56374:"meningitis", 54324:"food_poisoning", 
                             16372:"cold", 35249:"pharyngitis", 44274:"meningitis", 
                             74821:"food_poisoning", 94231:"unknown"}
    
    
    # Thre test patients
    yang = ({"coughing", "runny_nose", "sneezing"},{"headache","fever"})
    maria = ({"coughing", "fever", "sore_throat", "sneezing"},{"muscle_pain"})
    jaspal = ({"headache"},{"sneezing"})
    
#    # Testing the symptom_similarity function
#    print("*"*80)
#    sim = symptom_similarity(yang, maria)
#    print("The similarity between Yang and Maria is",sim)
#    sim = symptom_similarity(yang, jaspal)
#    print("The similarity between Yang and Jaspal is",sim)
#    sim = symptom_similarity(maria, jaspal)
#    print("The similarity between Maria and Jaspal is",sim)
#    
#    # Testing the similarity_to_patients function
#    print("*"*80)    
#    sim_list = similarity_to_patients(yang, all_patients_symptoms)
#    print("similarity list for Yang is ",sim_list)
#    sim_list = similarity_to_patients(maria, all_patients_symptoms)
#    print("Similarity list for Maria is ",sim_list)
#    sim_list = similarity_to_patients(jaspal, all_patients_symptoms)
#    print("Similarity list for Jaspal is ",sim_list)
##    
#    # Testing the most_similar_patients function
#    print("*"*80)
#    best_matches_yang = most_similar_patients(yang, all_patients_symptoms,3)
#    print("Yang's best matches:",best_matches_yang)
#    best_matches_maria = most_similar_patients(maria, all_patients_symptoms,4)
#    print("Maria's best matches:",best_matches_maria)
#    best_matches_jaspal = most_similar_patients(jaspal, all_patients_symptoms,4)
#    print("Jaspal's best matches:",best_matches_jaspal)
#    
#    # Testing the count_diagnostics function
#    print("*"*80)
#    diagnostics_yang = count_diagnostics({16372, 45437, 54324}, all_patients_diagnostics)
#    print("Diagnostics for Yang:", diagnostics_yang)
#    diagnostics_maria = count_diagnostics({35249, 16372, 74821, 94231}, all_patients_diagnostics)
#    print("Diagnostics for Maria:", diagnostics_maria)
#    diagnostics_jaspal = count_diagnostics({44274, 56374}, all_patients_diagnostics)
#    print("Diagnostics for Jaspal:", diagnostics_jaspal)
#    
#    # Testing the diagnostics_from_symptoms function
#    print("*"*80)    
#    diagnostics_yang = diagnostics_from_symptoms(yang, all_patients_symptoms, all_patients_diagnostics, 4)
#    print("Diagnostics for Yang:", diagnostics_yang)
#    diagnostics_maria = diagnostics_from_symptoms(maria, all_patients_symptoms, all_patients_diagnostics, 4)
#    print("Diagnostics for Maria:",diagnostics_maria)
#    diagnostics_jaspal = diagnostics_from_symptoms(jaspal, all_patients_symptoms, all_patients_diagnostics, 4)
#    print("Diagnostics for Jaspal:",diagnostics_jaspal)
###    
#    # Testing the pretty_print_diagnostics function
#    print("*"*80)
#    print("Patient Yang:")
#    pretty_print_diagnostics(diagnostics_yang)
#    print("Patient Maria:")
#    pretty_print_diagnostics(diagnostics_maria)
#    print("Patient Jaspal:")
#    pretty_print_diagnostics(diagnostics_jaspal)
##    
    # Testing the recommend_symptom_to_test function
#    print("*"*80)
#    rec_yang = recommend_symptom_to_test(yang, all_patients_symptoms, all_patients_diagnostics, 4)
#    print("Recommended symptom to test for Yang:",rec_yang)
#    rec_maria = recommend_symptom_to_test(maria,  all_patients_symptoms, all_patients_diagnostics, 4)
#    print("Recommended symptom to test for Maria:",rec_maria)
#    rec_jaspal = recommend_symptom_to_test(jaspal,  all_patients_symptoms, all_patients_diagnostics, 4)
#    print("Recommended symptom to test for Japsal:",rec_jaspal)

##
#    # Now doing the same tests on a much larger data set
#    print("*"*80)
#    print("Now with the larger patient data set...")
#    
#    all_patients_symptoms, all_patients_diagnostics = read_data_from_file("D:/Belle's Files 2018 0606/學校作業/2019-2020/Comp 204 assignments/3/medicalData.txt")    
#    print("All")
#    print(all_patients_symptoms)
#    
#    # Testing the similarity_to_patients function    
#    print("*"*80)
#    sim_list = similarity_to_patients(yang, all_patients_symptoms)
#    print("similarity list for Yang is ",sim_list)
#    sim_list = similarity_to_patients(maria, all_patients_symptoms)
#    print("Similarity list for Maria is ",sim_list)
#    sim_list = similarity_to_patients(jaspal, all_patients_symptoms)
#    print("Similarity list for Jaspal is ",sim_list)
#    
#    # Testing the most_similar_patients function
#    print("*"*80)    
#    best_matches_yang = most_similar_patients(yang, all_patients_symptoms,100)
#    print("Yang's best matches:",best_matches_yang)
#    best_matches_maria = most_similar_patients(maria, all_patients_symptoms,100)
#    print("Maria's best matches:",best_matches_maria)
#    best_matches_jaspal = most_similar_patients(jaspal, all_patients_symptoms,100)
#    print("Jaspal's best matches:",best_matches_jaspal)
#    
#    # Testing the diagnostics_from_symptoms function
#    print("*"*80)       
#    diagnostics_yang = diagnostics_from_symptoms(yang, all_patients_symptoms, all_patients_diagnostics, 100)
#    print("Diagnostics for Yang:", diagnostics_yang)
#    diagnostics_maria = diagnostics_from_symptoms(maria, all_patients_symptoms, all_patients_diagnostics, 100)
#    print("Diagnostics for Maria:",diagnostics_maria)
#    diagnostics_jaspal = diagnostics_from_symptoms(jaspal, all_patients_symptoms, all_patients_diagnostics, 100)
#    print("Diagnostics for Jaspal:",diagnostics_jaspal)
#    
#    # Testing the pretty_print_diagnostics function
#    print("*"*80)
#    print("Patient Yang:")
#    pretty_print_diagnostics(diagnostics_yang)
#    print("Patient Maria:")
#    pretty_print_diagnostics(diagnostics_maria)
#    print("Patient Jaspal:")
#    pretty_print_diagnostics(diagnostics_jaspal)
#    
#    # Testing the recommend_symptom_to_test function
#    print("*"*80)
#    rec_yang = recommend_symptom_to_test(yang, all_patients_symptoms, all_patients_diagnostics, 100)
#    print("Recommended symptom to test for Yang:",rec_yang)
#    rec_maria = recommend_symptom_to_test(maria,  all_patients_symptoms, all_patients_diagnostics, 100)
#    print("Recommended symptom to test for Maria:",rec_maria)
#    rec_jaspal = recommend_symptom_to_test(jaspal,  all_patients_symptoms, all_patients_diagnostics, 100)
#    print("Recommended symptom to test for Jaspal:",rec_jaspal)

    
my_test()