def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males = int(input('Enter number of male students: '))
    num_females = int(input('Enter number of female students: '))
    total = num_males + num_females
    m_perc = (num_males / total) *100
    f_perc = (num_females / total) *100
    print(num_males)
    print(num_females)
    print(total)
    print(f'Percentage of male students \t {m_perc: .2f}')
    print(f'Percentage of female students \t {f_perc: .2f}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
