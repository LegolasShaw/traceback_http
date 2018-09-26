from tracefile import write_error_http

if __name__ == "__main__":
    try:
        x = 10/0
    except Exception as err:
        write_error_http(__file__, err)
